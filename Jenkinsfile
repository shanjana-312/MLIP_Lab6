pipeline {
    agent any

    environment {
        CONDA = 'C:/Users/Public/Miniconda3'  
    }

    stages {
        stage('Set Up Conda Environment') {
            steps {
                bat '''
                call "%CONDA%/Scripts/activate.bat"
                call "%CONDA%/condabin/conda.bat" create -n mlip python=3.10 -y -c conda-forge
                call "%CONDA%/condabin/conda.bat" activate mlip
                pip install numpy pandas scikit-learn pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call "%CONDA%/Scripts/activate.bat"
                call "%CONDA%/condabin/conda.bat" activate mlip
                cd "%WORKSPACE%"
                pytest
                '''
            }
        }
    }
}
