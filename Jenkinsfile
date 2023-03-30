pipeline {
  agent {
    node {
      label "docker-agent-python-node"
    }
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