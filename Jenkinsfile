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
                sh 'sudo apt update && sudo apt install -y python3-pip'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install flask'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}

