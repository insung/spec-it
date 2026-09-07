# AWS Lambda benchmark

| Area | Measures |
| --- | --- |
| Demand | invocation rate, concurrency, payload and event source |
| Response | duration distribution, error, timeout |
| Runtime | cold start, init duration, memory allocation, max memory used |
| Capacity | concurrency, throttle, retry, downstream saturation |
| Cost | invocation, GB-second, event source, log and transfer unit cost |
| Operations | deploy, rollback, trace and failure-analysis time |

## Required decision prompts

- Is invocation synchronous, asynchronous, stream, queue, schedule, or another event source, and what are its delivery guarantees?
- Are handler timeout, client timeout, event visibility, downstream deadline, and retry count consistent?
- What input bounds, idempotency key, partial-failure behavior, dead-letter path, and concurrency limit apply?
- What project thresholds trigger review for duration headroom, maximum memory, throttle, retry, downstream saturation, cold start, and unit cost?
- Does VPC, secret, network, log, trace, or payload growth change the failure or cost model?
