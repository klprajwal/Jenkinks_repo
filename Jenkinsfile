pipeline {
    agent any
	
	stages {
	    stage('Install dependencies') {
		    steps {
			  sh 'echo "stage1"'
			  sh '''
			      python3 -m pip install --upgrade pip
                              python3 -m  pip install ncclient
                              python3 -m  pip install pandas
                              python3 -m  pip install ipaddress
                              python3 -m  pip install netaddr
                              python3 -m  pip install prettytable
			  '''
			}
		}
		stage('Checking and fixing') {   
		    steps {
			sh 'pylint netman_netconf_obj2.py'
                    }				
                }
		stage('Running application') {
		    steps {
			  sh 'echo "stage3"'
			}
		}
		stage('Unit test') {   
		     steps {
			  sh 'echo "stage4"'
             }				
        }
	}
}
