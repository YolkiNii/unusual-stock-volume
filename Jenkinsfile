pipeline {
  agent {
    node {
      label "docker-agent-python-node"
    }
  }
  triggers {
    pollSCM "*/5 * * * *"
  }
  stages {
    stage("Build") {
      steps {
        echo "In Build stage"
      }
    }
    stage("Test") {
      steps {
        echo "In Test stage"
      }
    }
  }
}