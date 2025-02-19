pipeline {
    agent any
    

    stages {
        
        stage('Check Environment') {
	    steps {
                sh 'hostname'  // Shows where Jenkins is running
            }
        }

	stage('Clone Repository') {
            steps {
                git 'https://github.com/Nandha172/first-jenkins-project.git'
            }
        }


        stage('Setup Python Environment') {
          steps {
	          sh '''
                    sudo apt-get update -y && \
		    sudo apt-get install -y python3 && \
                    sudo apt-get install -y python3-venv && \
                    sudo apt-get install -y python3-pip
                    
                    # Create venv if not exists
                    if [ ! -d "venv" ]; then
                        python3 -m venv venv
                    fi
                    
                    # Install dependencies
                    venv/bin/pip install --upgrade pip
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
          steps {
            script {
              sh 'nohup venv/bin/python app.py > flask.log 2>&1 &'
              sleep 5  // Wait a few seconds to ensure Flask starts properly
              sh 'ps aux | grep app.py'  // Check if the Flask process is running
            }
          }
        }

    }
}

