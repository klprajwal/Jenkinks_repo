pipeline {
    agent any
	
	stages {
	    stage('Install dependencies') {
		    steps {
			  sh 'echo "stage1"'
			  sh '''
			      python3 -m pip install --upgrade pip
			      python3 -m pip install pylint
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
			sh '''
			#!/bin/bash
                       pylint_score=$(python3 -m pylint netman_netconf_obj2.py | grep -o 'at .*10 ' | awk -F. '{print $1}' | grep -o '[0-9]*')
		       echo "$pylint_score"
                       if [ "$pylint_score" -lt 5 ]; then
                            echo "Pylint violation occurred: $pylint_score/10"
                            echo "Fix the violation before proceeding further"
                            exit 1
                       fi
			'''
                    }				
                }
		stage('Running application') {
		    steps {
			  sh 'python3 netman_netconf_obj2.py'
			}
		}
		stage('Unit test') {   
		     steps {
			  sh 'python3 -m unittest -v unit_test.py'
             }				
        }
	}
}
