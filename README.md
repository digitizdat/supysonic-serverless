# Supysonic

_Supysonic_ is a Python implementation of the [Subsonic](http://www.subsonic.org/pages/api.jsp] server API.

_Supysonic-Serverless_ is an experimental serverless implementation of _Supysonic_, currently targeting the AWS environment.

## Working notes
### Initial assessment - 6 Aug 20
* The Supysonic codebase is organized for execution with a web frontend to be used for administration. I'm going to bypass that in order to focus on getting the backend functions working in Lambda.
  * To this end, I've created the `requirements.txt` and `supyapi.py` files, which simplify deployment of just the API via [Zappa](https://github.com/Miserlou/Zappa).
  
* Database schema
  * The datbase schema hosts metadata about the files hosted in folders, presumably on a filesystem.
  * The current PostgreSQL schema is very file-oriented, but I don't see any major issues with using it as is to organize objects in an S3 bucket. I think we can push all of the logic changes into the Folder Manager.

* Folder Manager
  * I like how the Supysonic code has organized its structure for Flask, and especially how they've broken out the user management and folder management into the `managers` folder and assigned those functions to classes called FolderManager and UserManager.
  * I think we can genericize & modularize the FolderManager class to handle multiple types of backends.
     * Break out the current code into a filesystem FolderManager plugin/module
     * Create new code for an S3 plugin/module
