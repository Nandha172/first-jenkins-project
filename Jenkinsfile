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
                # Ensure Python, pip, and virtualenv are installed
                sudo apt-get update -y
                sudo apt-get install -y python3 python3-venv python3-pip

                # Create a virtual environment only if it doesn't exist
                if [ ! -d "venv" ]; then
                    python3 -m venv venv
                fi

                # Activate virtual environment and install dependencies
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                source venv/bin/activate && nohup python3 app.py &
                '''
            }
        }
    }
}


