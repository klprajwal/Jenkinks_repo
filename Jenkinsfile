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
			sh '''
			#!/bin/bash

			pylint netman_netconf_obj2.py > pylint_report.txt


			num_violations=$(grep 'Your code has been rated at' pylint_report.txt | awk '{print $7}' | awk -F "/" '{print $1}')

			#echo "$num_violations : test "

			conv_int=$(printf "%.0f" "$num_violations")
			#echo "$conv_int : the integer"
			# Checking if the number of violations exceeds the quality gate
			if [ "$conv_int" -gt 5 ]; then
			echo "pylint score: $num_violations/10"
			echo "pipeline can proceed"
			exit 0 
			else
			echo "Pylint violation occured: $num_violations/10"
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
