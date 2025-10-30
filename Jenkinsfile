pipeline {
    agent any
   
    stages {

        stage('Run S Tests with pytest') {
            steps {
                    echo "Running S Tests using pytest"

                    // Install Python dependencies
                    bat 'pip install -r requirements.txt'

                    // ✅ Start Flask app in background
                    bat 'start /B python app.py'

                    // ⏱️ Wait a few seconds for the server to start
                    bat 'ping 127.0.0.1 -n 5 > nul'

                    // ✅ Run tests using pytest
                    bat 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t sdemoapp:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                  bat 'docker login -u erumfaiz -p Erum@3005'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker tag sdemoapp:v1 erumfaiz/sample:seleniumtestimage"               
                bat "docker push erumfaiz/sample:seleniumtestimage"
            }
        }

        stage('Deploy to Kubernetes') { 
            steps { 
                    // apply deployment & service 
                    bat 'kubectl apply -f deployment.yaml --validate=false' 
                    bat 'kubectl apply -f service.yaml' 
            } 
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
