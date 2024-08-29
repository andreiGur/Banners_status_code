pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github-credentials') // This assumes you have added the PAT with this exact ID in Jenkins
    }

    stages {
        stage('Checkout Repository') {
            steps {
                // Checkout the code from your GitHub repository using the PAT
                git branch: 'main', 
                    url: 'https://github.com/andreiGur/Banners_status_code.git',
                    credentialsId: 'GITHUB_TOKEN' // Use the environment variable that holds the token
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment and install dependencies
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Python test script
                sh '''
                    source venv/bin/activate
                    python3 My_Python_Scripts/banners_test.py
                '''
            }
        }
    }

    post {
        always {
            // Clean up the workspace after the build within a node context
            node {
                cleanWs()
            }
        }
    }
}

