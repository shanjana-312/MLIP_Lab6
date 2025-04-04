pipeline {
    agent any

    environment {
        CONDA = 'C:/Users/Public/Miniconda3'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/shanjana-312/MLIP_Lab6.git'
            }
        }

        stage('Set Up Conda Environment') {
            steps {
                bat '''
                call "%CONDA%/Scripts/activate.bat"
                call "%CONDA%/condabin/conda.bat" env list | findstr mlip >nul
                if %ERRORLEVEL% NEQ 0 (
                    echo Creating 'mlip' environment...
                    call "%CONDA%/condabin/conda.bat" create -n mlip python=3.10 -y -c conda-forge
                )
                call "%CONDA%/condabin/conda.bat" install -n mlip numpy pandas scikit-learn pytest -y
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call "%CONDA%/Scripts/activate.bat"
                call "%CONDA%/condabin/conda.bat" activate mlip

                cd "%WORKSPACE%"
                set PYTHONPATH=%CD%
                echo PYTHONPATH is set to: %PYTHONPATH%

                python -c "import utility; print('utility.py is visible')"
                python -m pytest
                '''
            }
        }
    }
}
