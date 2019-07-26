pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                input id: 'Pass arguments', message: 'pass arguments', ok: 'done', parameters: [file(description: '', name: 'run.sh')]
            }
        }
    }
}