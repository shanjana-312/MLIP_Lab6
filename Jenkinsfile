pipeline {
    agent any

    stages {
        stage('Set Up Conda Environment') {
            steps {
                bat '''
                call C:\\Miniconda3\\Scripts\\activate.bat
                conda create -n mlip python=3.10 -y -c conda-forge
                call conda activate mlip
                pip install numpy pandas scikit-learn pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call C:\\Miniconda3\\Scripts\\activate.bat
                call conda activate mlip
                cd C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\mliplab6
                pytest
                '''
            }
        }
    }
}
