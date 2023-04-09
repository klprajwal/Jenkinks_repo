pipeline {
    agent any
	
	stages {
	    stage('Install dependencies') {
		    steps {
			  sh 'echo "stage1"'
			  pwd  
			}
		}
		stage('Checking and fixing') {   
		     steps {
			  sh 'echo "stage2"'
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
