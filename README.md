# robotframework-prerunmodifier-example
An example of a prerunmodifier

Run:
robot --pythonpath prerunmodifiers --prerunmodifier "TestDuplicator:S1:Precondition for S1:S2:Precondition for S2:S3:Precondition for S3" .