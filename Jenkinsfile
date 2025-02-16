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
                    python3 -m venv venv
                    bash -c "source venv/bin/activate"
                '''
            }
        }
        stage('Run Flask App') {
            steps {
                sh '''
                    source venv/bin/activate
                    python3 app.py
                '''
            }
        }
    }
}

