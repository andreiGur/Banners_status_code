pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Replace with your repository's URL
                git 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment
                sh 'python3 -m venv venv'
                
                // Activate the virtual environment
                sh 'source venv/bin/activate'
                
                // Upgrade pip and install dependencies
                sh 'venv/bin/pip install --upgrade pip'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the test script
                sh 'venv/bin/python3 your_test_script.py'
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
