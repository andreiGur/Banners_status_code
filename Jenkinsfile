pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('895e33aa-3d78-4a7e-b40c-4183a09e6adf') // Replace 'github-pat' with the actual ID you gave when adding the PAT
    }

    stages {
        stage('Checkout Repository') {
            steps {
                // Checkout the code from your GitHub repository using the PAT
                git branch: 'main', 
                    url: 'https://github.com/andreiGur/Banners_status_code.git',
                    credentialsId: 'github-pat' // Ensure this matches the ID of your PAT in Jenkins
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment and install dependencies
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Python test script
                sh 'source venv/bin/activate && python3 My_Python_Scripts/your_test_script.py'
            }
        }
    }

    post {
        always {
            // Clean up the workspace after the build
            cleanWs()
        }
    }
}
