pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Nandha172/first-jenkins-project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    sudo apt-get update -y
                    sudo apt-get install -y python3 python3-venv python3-pip
                    
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
                sh '''
                    # Run Flask app using venv's Python
                    venv/bin/python app.py
                '''
            }
        }
    }
}

