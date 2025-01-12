import EmailInput from "@/components/common/EmailInput";
import Container from "@/components/Container";

export default function Home() {
  return (
    <Container className="py-10 flex flex-col items-center justify-center h-screen">
      <EmailInput />
    </Container>
  );
}
