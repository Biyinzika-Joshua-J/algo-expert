# min:48

class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])
    
    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        # add edges
        graph.addPrereq(job, prereq)

    return graph


def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        pass

def topological_sort_dfs(jobs, deps): # find one order in which these jobs can be completed that will respect their dependency
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def topological_sort_bfs(jobs, deps): # find one order in which these jobs can be completed that will respect their dependency
    pass


jobs = [1,2,3,4] # answers => [1,4,3,2] or [4,1,3,2]
dependencies = [[1,2], [1,3], [3,2], [4,2], [4,3]] # first job is a prerequisite to the second job 





