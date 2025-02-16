pipeline {
    agent any

    environment {
        PYTHON_ENV = "venv" // Virtual environment name
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Nandha172/first-jenkins-project.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                sh '''
                python3 -m venv $PYTHON_ENV
                source $PYTHON_ENV/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source $PYTHON_ENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Previous Flask App') {
            steps {
                sh '''
                pkill -f "python3 app.py" || true
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                source $PYTHON_ENV/bin/activate
                nohup python3 app.py > flask_app.log 2>&1 &
                '''
            }
        }
    }
}
