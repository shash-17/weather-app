pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install pytest --break-system-packages --quiet || pip3 install pytest --quiet || true'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 weather.py'
            }
        }
        stage('Automated Test Suite') {
            steps {
                sh 'python3 -m pytest test_weather.py -v'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
                sh 'kubectl rollout status deployment/weather-app'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'weather.py', fingerprint: true
        }
        success {
            echo 'Pipeline Succeeded: App tested, artifact archived, and deployed to Kubernetes.'
        }
        failure {
            echo 'Pipeline Failed: Quality Gate triggered. Deployment halted.'
        }
    }
}
