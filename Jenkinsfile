pipeline {
    agent any
    stages {
        stage('Install Python Dependencies') {
            steps {
                script {
                    // Define the list of Python packages to install
                    def pythonPackages = ['nccclient', 'pandas', 'ipaddress', 'netaddr', 'prettytable']
                    
                    // Loop through the packages and install them using pip
                    for (def package : pythonPackages) {
                        sh "pip install ${package}"
                    }
                }
            }
        }
        // Add more stages as p 
    }
}
