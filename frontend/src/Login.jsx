import { useState } from "react";

function Login() {
  const [isRegister, setIsRegister] = useState(false);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    if (isRegister) {
      alert("Registration UI is working!");
    } else {
      alert("Login UI is working!");
    }
  };

  return (
    <div className="auth-page">

      <div className="auth-glow auth-glow-one"></div>
      <div className="auth-glow auth-glow-two"></div>

      <div className="auth-card">

        <div className="auth-logo">
          <span>✦</span>
          Resume<span className="blue">AI</span>
        </div>

        <div className="auth-header">

          <div className="section-label">
            {isRegister ? "CREATE ACCOUNT" : "WELCOME BACK"}
          </div>

          <h1>
            {isRegister
              ? "Create your account"
              : "Welcome back"}
          </h1>

          <p>
            {isRegister
              ? "Start improving your resume today."
              : "Sign in to continue to ResumeAI."}
          </p>

        </div>

        <form onSubmit={handleSubmit}>

          {isRegister && (
            <div className="form-group">

              <label>
                Full Name
              </label>

              <input
                type="text"
                placeholder="Enter your name"
                value={name}
                onChange={(event) =>
                  setName(event.target.value)
                }
                required
              />

            </div>
          )}

          <div className="form-group">

            <label>
              Email
            </label>

            <input
              type="email"
              placeholder="you@example.com"
              value={email}
              onChange={(event) =>
                setEmail(event.target.value)
              }
              required
            />

          </div>

          <div className="form-group">

            <label>
              Password
            </label>

            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(event) =>
                setPassword(event.target.value)
              }
              required
            />

          </div>

          <button
            type="submit"
            className="auth-button"
          >
            {isRegister
              ? "Create Account →"
              : "Login →"}
          </button>

        </form>

        <div className="auth-switch">

          <span>
            {isRegister
              ? "Already have an account?"
              : "Don't have an account?"}
          </span>

          <button
            type="button"
            onClick={() =>
              setIsRegister(!isRegister)
            }
          >
            {isRegister
              ? "Login"
              : "Register"}
          </button>

        </div>

        <a
          href="/"
          className="back-home"
        >
          ← Back to Resume Analyzer
        </a>

      </div>

    </div>
  );
}

export default Login;