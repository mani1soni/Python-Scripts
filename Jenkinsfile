pipeline{
    agent any
    def output=input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]

    stages{
        stage("test"){
            steps{
                sh '''
                sh run.sh ${output}
                '''
            }
        }
    }
}