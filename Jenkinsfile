pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                git url: 'https://github.com/Arushi9740/sepp07.git', branch: 'main'
            }
        }

        stage('Setup Dependencies') {
            steps {
                echo "Setting up Python virtual environment and installing dependencies"
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }

        stage('Function') {
            steps {
                echo "Executing otp.py"
                bat '''
                call venv\\Scripts\\activate
                python sepp03.py
                '''
            }
        }

        stage('Test file') {
            steps {
                echo "Running test_otp.py"
                bat '''
                call venv\\Scripts\\activate
                pytest test03.py
                '''
            }
        }
    }
}
