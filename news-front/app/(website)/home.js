import Link from "next/link";
import Container from "@/components/container";
import PostList from "@/components/postlist";

export default function Post({ posts }) {
  return (
    <>
      {posts && (
        <Container>
          <div className="mt-10 grid gap-10 md:grid-cols-3 lg:gap-10 xl:grid-cols-3 ">
            {posts.map(post => (
              <PostList key={post._id} post={post} aspect="square" />
            ))}
          </div>
        </Container>
      )}
    </>
  );
}
