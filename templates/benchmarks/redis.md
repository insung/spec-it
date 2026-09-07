# Redis benchmark

| Area | Measures |
| --- | --- |
| Demand | command mix, key size, read/write rate, connection count |
| Response | latency distribution, timeout, error |
| Memory | used memory, fragmentation, growth, maxmemory |
| Policy | hit ratio, miss ratio, eviction, TTL distribution, stale tolerance |
| Reliability | failover, reconnect, warm-up and source-of-truth recovery |
| Cost | memory capacity, transfer, operation and recovery time |

## Required decision prompts

- Why is Redis required instead of process memory, the source database, a queue, or direct computation?
- What is the source of truth, and how does the application behave after a miss, eviction, expiration, failover, or total loss?
- What are the key cardinality, key and value size distributions, TTL, invalidation, stale tolerance, and privacy deletion contract?
- Which fields are unnecessary before considering a compact encoding or abbreviated physical schema?
- What project thresholds trigger review for memory, growth, fragmentation, hit ratio, eviction, latency, connections, and unit cost?
