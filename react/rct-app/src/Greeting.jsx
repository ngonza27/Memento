export function Greeting(props) {
  console.log(props)
  const { title } = props
  return <div>Componente {title}</div>;
  }
export function UserCard(props) {
  console.log(props.greet)
  return <div>UserCard</div>;
}
