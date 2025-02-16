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
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install flask'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}

