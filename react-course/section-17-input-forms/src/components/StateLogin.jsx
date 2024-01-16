import Input from "./Input";
import { isEmail, isNotEmpty, hasMinLength } from '../util/validation'
import { useInput } from "../hook/useInput";

export default function Login() {
  const {
    value: emailValue,
    handleInputChange: handleEmailChange,
    handleBlur: handleEmailBlur,
    hasError: emailHasError,
  } = useInput('', (value) => isEmail(value) && isNotEmpty(value)
  )

  const {
    value: passwordValue,
    handleInputChange: handlePasswordChange,
    handleBlur: handlePasswordBlur,
    hasError: passwordHasError
  } = useInput('', (value) => hasMinLength(value, 6))


  function handleSubmit(event) {
    event.preventDefault()
    if (emailHasError || passwordHasError) {
      return
    }
    console.log(emailValue, passwordValue)
  }


  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>

      <div className="control-row">
        <Input
          label="Email"
          id="email"
          type="email"
          name="email"
          error={emailHasError && 'Please enter a valid email'}
          onBlur={handleEmailBlur}
          onChange={handleEmailChange}
          value={emailValue}
        />
        <Input
          label="Password"
          id="password"
          type="password"
          name="password"
          error={passwordHasError && 'Please enter a valid password'}
          onBlur={handlePasswordBlur}
          onChange={handlePasswordChange}
          value={passwordValue}
        />
      </div>

      <p className="form-actions">
        <button className="button button-flat">Reset</button>
        <button className="button">Login</button>
      </p>
    </form>
  );
}
