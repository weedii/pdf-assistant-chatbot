import Container from "@/components/Container";
import UploadFile from "@/components/UploadFile";
import Image from "next/image";

export default function Home() {
  return (
    <Container className="py-10">
      <UploadFile />
    </Container>
  );
}
