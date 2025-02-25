pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nandha172/flask-app"  // Replace with your Docker Hub username and repo
        CONTAINER_NAME = "flask_container"
    }

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

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $DOCKER_IMAGE .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u nandha172 --password-stdin
                    '''
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh '''
                    docker push $DOCKER_IMAGE
                '''
            }
        }

        stage('Run Flask Container') {
            steps {
                sh '''
                    # Stop and remove existing container if running
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true

                    # Run the new container
                    docker run -d --name $CONTAINER_NAME -p 5000:5000 $DOCKER_IMAGE
                '''
            }
        }
    }
}

