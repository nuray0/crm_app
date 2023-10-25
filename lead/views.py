import csv

from typing import Any, Dict
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.db.models.query import QuerySet
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.views import View

from .forms import AddCommentForm, AddFileForm
from .models import Lead

from client.models import Client, Comment as ClientComment

from team.models import Team


class LeadsExportView(LoginRequiredMixin, View):

    class Meta:
        model = Lead

    def get(self, *args, **kwargs):
        leads = Lead.objects.filter(created_by=self.request.user)
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="leads.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(["Lead", "Email", "Description",
                         "Priority", "Status", "Converted_to_client",
                        "Created_at", "Created_by"])

        for lead in leads:
            writer.writerow([lead.name, lead.email, lead.description,
                             lead.priority, lead.status, lead.converted_to_client,
                            lead.created_at, lead.created_by])

        return response


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(LeadListView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, converted_to_client=False)


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm()
        context['fileform'] = AddFileForm()
        return context

    def get_object(self):
        obj = super().get_object()
        return obj


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:index')


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    fields = ['name', 'email', 'description', 'priority', 'status']
    success_url = reverse_lazy('leads:index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['team'] = self.request.user.userprofile.active_team
        context['title'] = 'Add lead'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = self.request.user.userprofile.active_team
        self.object.save()
        return redirect(self.get_success_url())


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    fields = ['name', 'email', 'description', 'priority', 'status']

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit lead'
        return context

    def get_success_url(self):
        lead = super().get_object()
        return reverse_lazy('leads:index')


class ConvertToClientView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        lead = get_object_or_404(
            Lead, created_by=request.user, pk=self.kwargs.get('pk'))
        team = request.user.userprofile.active_team
        clients = Client.objects.filter(created_by=request.user)

        if len(clients) < team.plan.max_clients:

            client = Client.objects.create(
                name=lead.name,
                email=lead.email,
                description=lead.description,
                created_by=request.user,
                team=team,
            )

            # convert lead comments to client comments
            comments = lead.comments.all()
            for comment in comments:
                ClientComment.objects.create(
                    team=comment.team,
                    client=client,
                    content=comment.content,
                    created_by=comment.created_by,
                )

            # delete the lead after converting it to a client
            lead.converted_to_client = True
            lead.delete()

            messages.success(request, 'The lead was converted to a client')

        else:
            messages.error(
                request, 'Your team has reached maximum number of clients. Your owner must upgrade your plan!')

        return redirect('leads:index')


class AddFileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.team = request.user.userprofile.active_team
            file.created_by = request.user
            file.lead_id = pk
            file.save()

        return redirect('leads:detail', pk=pk)


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = request.user.userprofile.active_team
            comment.created_by = request.user
            comment.lead_id = pk
            comment.save()

        return redirect('leads:detail', pk=pk)
