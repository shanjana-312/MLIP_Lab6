pipeline {
    agent any

    environment {
        CONDA = 'C:/Users/Public/Miniconda3'  
    }

    stages {
        stage('Set Up Conda Environment') {
            steps {
                bat '''
                call "C:/Users/Public/Miniconda3/Scripts/activate.bat"
                call C:/Users/Public/Miniconda3/condabin/conda.bat create -n mlip python=3.10 -y -c conda-forge
                call C:/Users/Public/Miniconda3/condabin/conda.bat install -n mlip numpy pandas scikit-learn pytest -y
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call "C:/Users/Public/Miniconda3/Scripts/activate.bat"
                call C:/Users/Public/Miniconda3/condabin/conda.bat activate mlip
                set PYTHONPATH=.
                cd "%WORKSPACE%"
                pytest
                '''
            }
        }

    }
}
