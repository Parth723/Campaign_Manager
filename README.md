# Campaign_Manager

There are two models: Subcriber and Campaign
The user must provide the name, email address and also select the subscribe to blog checkbox

Once selected, the next page asks for confirmation for sending an email with the blog.

After the confirmation the user with 'is_active' status as True, the email is sent with the following fields: Subject, html_content, etc.
We then land on the email_sent page.

If the status is False, you won't receive the blogs.
