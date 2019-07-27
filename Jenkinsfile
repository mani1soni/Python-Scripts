output=input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]

pipeline{
    agent any
    stages{
        stage("test"){
            script{
                output=input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]
            }
            steps{
                sh '''
                sh run.sh ${output}
                '''
            }
        }
    }
}