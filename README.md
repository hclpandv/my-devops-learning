## Clone repo

    git clone ssh://ec2-user@35.156.211.147:/srv/git/slot.git

 

## Build distribution package

    npm run build:rpm

RPM requires httpd and installs the following files/directories to the /var/www/html directory:

    ./images/**/*
    ./index.html
    ./js/**/*

 
Created RPM will be located here

    ./build/RPMS/x86_64/netent-slot-1.0.1-1.el7.centos.x86_64.rpm

 

## To run application

    Install httpd:
    sudo yum install httpd

    Install created rpm, e.g.:
     sudo rpm -ip netent-slot-1.0.1-1.el7.centos.x86_64.rpm


## To develop/test locally, use Vagrant (runs CentOS)

    ''' 
    vagrant plugin install vagrant-vbguest // to install VirtualBox Guest Additions automatically.
    vagrant up
    vagrant ssh
    '''

 

## To deploy
Pushing to origin and trigger the build on Jenkins, http://35.159.8.210:8080/job/slot-master-pl/

TODO: Automate this at last! Trigger pipeline job on commit.