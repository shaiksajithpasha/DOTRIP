import { useState } from "react";
import { useNavigate } from "react-router-dom";
import type { SubmitEvent } from "react";
import "./Login.css";

interface LoginResponse {
  access_token: string;
  token_type: string;
  user: {
    id: number;
    name: string;
    email: string;
    phone: string | null;
    role: string;
  };
}

function Login() {
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  const navigate = useNavigate();

  const handleLogin = async (e: SubmitEvent) => {
    e.preventDefault();

    setError("");
    setLoading(true);

    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/login`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            identifier,
            password,
          }),
        }
      );

      const data: LoginResponse | { detail: string } =
        await response.json();

      // Check exactly what the backend returned
      console.log("LOGIN RESPONSE:", data);

      if (!response.ok) {
        throw new Error(
          "detail" in data ? data.detail : "Login failed"
        );
      }

      if ("access_token" in data) {
        // Save access token
        localStorage.setItem(
          "token",
          data.access_token
        );

        // Save user information
        localStorage.setItem(
          "user",
          JSON.stringify(data.user)
        );

        console.log(
          "ACCESS TOKEN:",
          data.access_token
        );

        console.log(
          "USER:",
          data.user
        );

        console.log(
          "TOKEN SAVED:",
          localStorage.getItem("token")
        );

        // Redirect to dashboard
        navigate("/dashboard", {
          replace: true,
        });
      }
    } catch (error) {
      if (error instanceof Error) {
        setError(error.message);
      } else {
        setError("Something went wrong");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="login-page">

      {/* LEFT SIDE */}
      <section className="login-visual">
        <div className="visual-overlay" />

        <div className="brand">
          <img
            src="/gemini-svg.svg"
            alt="DOTRIP"
            className="logo"
          />
        </div>

        <div className="visual-content">
          <span className="eyebrow">
            TRAVEL • EXPLORE • EXPERIENCE
          </span>

          <h1>
            Your journey
            <br />
            starts here.
          </h1>

          <p>
            Manage your trips, discover new destinations,
            and make every journey memorable.
          </p>
        </div>

        <div className="visual-footer">
          <span>© 2026 DOTRIP</span>
          <span>Travel smarter.</span>
        </div>
      </section>

      {/* LOGIN SIDE */}
      <section className="login-section">
        <div className="login-card">

          {/* MOBILE LOGO */}
          <div className="mobile-brand">
            <img
              src="/gemini-svg.svg"
              alt="DOTRIP"
              className="logo"
            />
          </div>

          {/* HEADING */}
          <div className="login-heading">
            <span className="login-eyebrow">
              WELCOME BACK
            </span>

            <h2>Sign in</h2>

            <p>
              Enter your credentials to continue to your
              account.
            </p>
          </div>

          {/* FORM */}
          <form onSubmit={handleLogin}>

            {/* EMAIL / PHONE */}
            <div className="form-group">
              <label htmlFor="identifier">
                Email or phone number
              </label>

              <div className="input-wrapper">
                <span className="input-icon">
                  @
                </span>

                <input
                  id="identifier"
                  type="text"
                  value={identifier}
                  onChange={(e) =>
                    setIdentifier(e.target.value)
                  }
                  placeholder="Enter email or phone"
                  autoComplete="username"
                  required
                />
              </div>
            </div>

            {/* PASSWORD */}
            <div className="form-group">
              <div className="password-label">
                <label htmlFor="password">
                  Password
                </label>
              </div>

              <div className="input-wrapper">
                <span className="input-icon">
                  •••
                </span>

                <input
                  id="password"
                  type={
                    showPassword
                      ? "text"
                      : "password"
                  }
                  value={password}
                  onChange={(e) =>
                    setPassword(e.target.value)
                  }
                  placeholder="Enter your password"
                  autoComplete="current-password"
                  required
                />

                <button
                  type="button"
                  className="password-toggle"
                  onClick={() =>
                    setShowPassword(
                      (previous) => !previous
                    )
                  }
                  aria-label={
                    showPassword
                      ? "Hide password"
                      : "Show password"
                  }
                >
                  {showPassword ? "Hide" : "Show"}
                </button>
              </div>
            </div>

            {/* ERROR */}
            {error && (
              <div className="login-error">
                <span>!</span>
                <p>{error}</p>
              </div>
            )}

            {/* LOGIN BUTTON */}
            <button
              className="login-button"
              type="submit"
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className="spinner" />
                  Signing in...
                </>
              ) : (
                <>
                  Sign in
                  <span className="button-arrow">
                    →
                  </span>
                </>
              )}
            </button>
          </form>

          {/* NOTE */}
          <p className="login-note">
            Access is managed by your DOTRIP
            administrator.
          </p>

        </div>
      </section>

    </main>
  );
}

export default Login;