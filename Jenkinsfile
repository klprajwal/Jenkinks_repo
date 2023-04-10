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
                        # Run pylint and store the output in a variable
                        pylint_report=$(python3 -m pylint netman_netconf_obj2.py | grep "Your code has been .*")
                        echo "${pylint_report}"

                        # Extract the number of violations from the pylint report
                        num_violations=$(echo "${pylint_report}" | grep 'Your code has been rated at' | awk '{print $7}' | awk -F "/" '{print $1}')

                        #echo "$num_violations : test "

                        # Convert the number of violations to an integer
                        conv_int=$(printf "%.0f" "$num_violations")
                        #echo "$conv_int : the integer"

                        # Checking if the number of violations exceeds the quality gate
                       if [ "$conv_int" -gt 5 ]; then
                       echo "pylint score: $num_violations/10"
                       echo "pipeline can proceed"
                       exit 0
                       else
                       echo "Pylint violation occurred: $num_violations/10"
                       echo "Fix the violation before proceeding further"
                       exit 1
                       fi
			'''
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
