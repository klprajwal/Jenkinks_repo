pipeline {
    agent any
	
	stages {
	    stage('Install dependencies') {
		    steps {
			    echo 'stage1'
			}
		}
		stage('Checking and fixing') {   
		     steps {
			    echo 'stage2'
             }				
        }
		stage('Running application') {
		    steps {
			    echo 'stage1'
			}
		}
		stage('Unit test') {   
		     steps {
			    echo 'stage2'
             }				
        }
	}
}
