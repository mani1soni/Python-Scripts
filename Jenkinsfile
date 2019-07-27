pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                def output = input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]
                sh '''
                sh run.sh $output
                '''
            }
        }
    }
}