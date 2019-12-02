#   Two Green Dogs   #

There's always lots to do... Starting off with a blog...

If you want to run the environment locally and you are ready to clone the repo, follow these steps:

  - But first create your project directory, usually <code>C:\Development\Workspace\\<project_name></code>
  - Copy the repo-url from this Github repo using the clone or download button.
  - The easiest is to plug the copied url into Github Desktop, clone / download it onto your PC (specific location) and off you go.
  - You will need to download and install python 3.7.x
  - Pip (the python package manager) which usually comes with python can install all dependencies and python / django packages. So once installed run these commands: <code>pip install django</code> & <code>pip install wagtail</code>
  - Now this part can be tricky or dead easy if you succeeded with the above. 
  - After downloading and installing requirements / dependencies onto your PC, run this command from the cmd prompt at your [project_name] PROJECT DIRECTORY: <code>pipenv run python manage.py runserver</code> 
  
  That should runserver for you, just hop onto your browser and type the address <code>localhost:8000</code> to view the site.
  Happy fiddling! (please give me a shout if you need help ;)
