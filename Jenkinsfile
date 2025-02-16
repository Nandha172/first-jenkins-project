pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Nandha172/first-jenkins-project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    sh 'sudo apt-get update -y'
                    sh 'sudo apt-get install -y python3 python3-venv python3-pip'
                    sh 'python3 -m venv venv'
                    sh 'venv/bin/pip install --upgrade pip'
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Flask App') {
            steps {
                script {
                    // Ensure the Flask app binds to all IP addresses (0.0.0.0) and a visible port
                    sh 'nohup venv/bin/python app.py &'
                    sleep(time: 5, unit: 'SECONDS') // Wait a moment to ensure Flask app starts

                    // Check if the Flask app is running
                    sh 'ps aux | grep app.py'
                }
            }
        }

        stage('Expose Flask App Logs') {
            steps {
                script {
                    // Tail the logs to ensure output is visible in Jenkins console
                    sh 'tail -f nohup.out'
                }
            }
        }
    }
}

