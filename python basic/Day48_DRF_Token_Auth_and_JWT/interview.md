# Day 48 — Real-World Backend Engineering Interview

These questions test your understanding of distributed authentication, token security, and session revocation.

---

### Question 1: How Do You Revoke a Stateless JWT If a User Clicks "Log Out of All Devices"?
**Interview Scenario:**
> *"If JWTs are stateless and verified without database queries, how does your backend immediately invalidate a user's access tokens when they change their password or click 'Log out of all devices'?"*

#### Senior Mentor Answer & Key Points:
1. **The Core Dilemma**:
   - Pure stateless JWTs cannot be revoked without introducing state somewhere.
2. **Industry Solution 1: Short Lifespans + Refresh Blacklisting**:
   - Make `access_token` lifespan very short (e.g. 5 minutes).
   - Invalidate the user's refresh token in Redis immediately upon logout.
   - Within 5 minutes, their existing access token naturally expires and cannot be refreshed.
3. **Industry Solution 2: User `jwt_version` / `token_created_after` Claim**:
   - Store a simple integer `jwt_version` on the User database model (cached in Redis).
   - Embed `jwt_version` in the JWT payload.
   - When the user clicks "Log out all devices", increment their `jwt_version` in Redis.
   - The token verification middleware compares the token's version with the Redis version. If it's stale, the token is instantly rejected!

---

### Question 2: Why `localStorage` is Dangerous for JWT Storage
**Interview Scenario:**
> *"Where should frontend single-page applications (React/Vue) store JWT access and refresh tokens?"*

#### Senior Mentor Answer & Key Points:
1. **The `localStorage` Hazard**:
   - Any JavaScript code running on the domain (including third-party analytics, chat widgets, or compromised NPM dependencies) has full access to `localStorage.getItem('token')`.
   - A single Cross-Site Scripting (XSS) vulnerability allows attackers to exfiltrate tokens.
2. **The Modern Architecture (BFF or HttpOnly Cookies)**:
   - **Access Token**: Kept in JavaScript memory (React state / closure). When the page refreshes, a silent refresh is triggered.
   - **Refresh Token**: Stored in a `Set-Cookie` header with `HttpOnly; Secure; SameSite=Strict`. JavaScript cannot read this cookie, eliminating XSS theft.
