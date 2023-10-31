# A CRM app, where you can create leads, clients and manage them

# This is a CRM app that allows to:

1. Sign up
2. Log in
3. Apply CRUD operations to leads
4. Apply CRUD operations to clients
5. Convert leads to clients
6. Change the pre-assigned, default team name
7. Change teams, if the user is a member of more than 1 team
8. Apply restrictions to numbers of allowed leads and clients for the basic, default plan

## The front page

<p align="center">
    <img style="width:100%" src="src/images-readme/front-page.jpg">
</p>

## The about page

<p align="center">
    <img style="width:100%" src="src/images-readme/about-page.jpg">
</p>

## The sign up page

<p align="center">
    <img style="width:100%" src="src/images-readme/signup-page.jpg">
</p>

## The login page

<p align="center">
    <img style="width:100%" src="src/images-readme/login-page.jpg">
</p>

<!--Team-->

## Team

When a user signs up, a new team gets created with the name "The team name" and the user is added as a member of this team. After logging in, the user can edit the team name or switch teams, if the user is a member of more than 2 teams.

<p align="center">
    <img style="width:100%" src="src/images-readme/team/team-details.jpg">
</p>

Editing the team name, to Superteam in this case:

<p align="center">
    <img style="width:100%" src="src/images-readme/team/team-edit.jpg">
</p>

When an action was successful, the app returns the user to the account page and prints out a success message:

<p align="center">
    <img style="width:100%" src="src/images-readme/team/team-edit-success.jpg">
</p>

By pressing on the "Switch team" button on team's details page, he user can view the list of teams the user is a member of. A team can be activated by pressing "Activate team" button:

<p align="center">
    <img style="width:100%" src="src/images-readme/team/team-switch.jpg">
</p>

The active team gets green background:

<p align="center">
    <img style="width:100%" src="src/images-readme/team/team-switch-success.jpg">
</p>

<!--Leads-->

## Leads

Currently there are no leads:

<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-empty.jpg">
</p>

A lead can be created by filling this form, there are drop-down lists for priority and status of the lead:

<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-add.jpg">
</p>

List of leads with priority and status:

<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-list.jpg">
</p>
 
 Users automatically get basic plan when signing up, which allows having up to 2 leads and 2 clients. If the user tries to create more than that, an error message will get printed:
<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-limit.jpg">
</p>

By clicking on the lead, details of the lead can be viewed. A lead can be converted to a client, edited, or deleted.

<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-details.jpg">
</p>

Editing a lead:

<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-edit.jpg">
</p>

After a successful action on a lead, the user gets returned to leads list and a success message is printed.

<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-converted-to-client.jpg">
</p>

By clicking on the "Export leads" button, a csv file will be downloaded with the leads' details on the leads list.

<p align="center">
    <img style="width:100%" src="src/images-readme/lead/lead-export-csv.jpg">
</p>

<!--Clients-->

## Clients

The functionality is similar for clients. Unlike leads, clients do not have priority and status fields.
A client can be created by:

1. Converting a lead to a client.
2. Creating a client by filling the form.
<p align="center">
    <img style="width:100%" src="src/images-readme/client/client-list.jpg">
</p>

A user can leave comments under each client's page:

<p align="center">
    <img style="width:100%" src="src/images-readme/client/client-details.jpg">
</p>

There is also a functionality for uploading files. Files can be downloaded by clicking on the "Download" button.

<p align="center">
    <img style="width:100%" src="src/images-readme/client/client-comments-and-files.jpg">
</p>
