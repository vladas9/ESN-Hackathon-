import HomePage from "./home";
import { getAllPosts } from "@/lib/sanity/client";

/**
 * 
 * post {
 *   categories: 
 *   title: string
 *   _createdAt: Date
 *   publishedAt: Date
 *   slug: {
 *     current
 *   }
 *   mainImage: {
 *     image
 *     blurDataURL
 *   }
 *   author: {
 *     name
 *     slug: {
 *       current
 *     }
 *     image
 *   }
 * }
 */

export default async function IndexPage() {
  // const posts = await getAllPosts();
  const post = {
    title: "Test Title",
    publishedAt: new Date(Date.now()).toISOString(),
    slug: {
      current: "0001"
    },
    mainImage: {
      image: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg",
      blurDataURL: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg"
    },
    author: {
      name: "Viorel Bostan",
      image: "https://media.licdn.com/dms/image/C4D03AQHdW_nAv9RKdw/profile-displayphoto-shrink_800_800/0/1579156231812?e=1705536000&v=beta&t=L9TZjXR3fE543IdT2NnU1xmK_zkelUcvhjJA3xoafZk",
      //image: "https://cdn.sanity.io/images/cijrdavx/production/05951a0ec1a6ffc54f615ab160649e92fea982d0-800x764.png?rect=0,0,800,468&w=800&auto=format",
      
      slug: {
        current: "Viorel Bostan"
      }
    }
  };
  const posts = [
    post, post, post, post,post, post, post, post,post, post, post, post  
  ];
  return <HomePage posts={posts} />;
}

// export const revalidate = 60;
