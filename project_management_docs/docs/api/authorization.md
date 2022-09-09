## Create a new user
To create a new user (employee), go to `/users/create`. The interface allows to specify various fields such as first name, last name, etc. 

## Authorization
Users are authorized by their usernames and password. They can also be identified by an authentification token. 
To get one, go to `/auth/token/login`.

## Edit user data
To update user information a user, go to `/auth/users/me`. 
You will be able to fill in the fields that have previously been empty or change the values of previously filled ones.