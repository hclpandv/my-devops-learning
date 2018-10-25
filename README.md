# Assignment for Technical Interview 

The Goal was to restore all the missing pieces of a damaged infrastructure consists of a Jenkins server, a Git server and a Static server (where an application was deployed erlier and running as of now)  

the application currently running at http://18.195.116.69/

## How the goal is achieved

* the git server is re-stored uisng the tar file provided to me via a cloud link.
* below command can be used to clone the repository on any workstation . make sure you have ssh keys in place on your system.

    git clone ssh://ec2-user@54.93.218.82:/srv/git/slot.git
    
* the package.json was re-stored from `./build/SOURCE` folder which had missing links to call and execute `buildRpm.sh` script to build the RPM.

* a seperate `deployRpm.sh` file is written to deploy the RPM package build.

* the jenkins server was missing all previous configuration and hence a new pipeline project was created to achieve the expeceted flow.

* pipeline project is using the git-server repo and a scripted `Jenkinsfile` is created on the root of the repo.

* the credentials of `ec2-user` and `jenkins-job` was already found preserved in the Jenkins UI. same is used in the pipeline.

* pipe line contains two stages i.e. `build` and `deploy`

* the pipeline is configured with SCM Polling to achive pipeline trigger on every git commit.

* the git hook `post-commit` is used to report the jenkins back about commit through curl api call.

* tried achiving traceability and reproducibility of RPM, using git tags with conditionalized stage i.e. `when { tag "release-v*"}` / `when {changelong 'release*'}` Not succeeded in this within the given timeframe. hence submitting.

* the Jenkins pipeline is tested with successful build and deploy stages 
* the application currently running at http://18.195.116.69/ after pipline trigger.

Thanks for the learning oportunity provided with this assignment.
