def output=input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]

pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                sh '''
                sh run.sh $output
                '''
            }
        }
    }
}