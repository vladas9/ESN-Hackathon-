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

function dbToObj(obj) {
  console.log(obj);
  return {
    title: obj.theme,
    publishedAt: obj.date, 
    slug: {
      current: obj.id,
    },
    mainImage: {
      image: obj.image
    },
    author: {
      name: obj.party.party_name,
      image: obj.party.party_logo,
      slug: {
        current: obj.party.id
      }
    }  
  }
}

export default async function IndexPage() {
  const posts = await fetch('http://127.0.0.1:5000/news')
    .then(req => req.json())
    .then(res => res.map(dbToObj));
  // console.log(posts);
  // const posts = await getAllPosts();
  // const post1 = {
  //   title: "Măsuri urgente în fata avertismentului meteorologic. Ion Ceban:”Serviciile municipale intervin în teren”",
  //   publishedAt: new Date(Date.now()).toISOString(),
  //   slug: {
  //     current: "masuri-urgente-in-fata-avertismentului-meteorologic"
  //   },
  //   mainImage: {
  //     image: "https://ionceban.md/wp-content/uploads/2023/11/ion_ceban_curatenia.jpg",
  //     blurDataURL: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg"
  //   },
  //   author: {
  //     name: "MAN",
  //     image: "https://ionceban.md/favicon.ico",
  //     slug: {
  //       current: "man"
  //     }
  //   }
  // };
  // const post2 = {
  //   title: "Igor Grosu: Alegând un primar PAS, primar european, ne apropiem tot mai mult de aderarea la Uniunea Europeană",
  //   publishedAt: new Date(Date.now()).toISOString(),
  //   slug: {
  //     current: "igor-grosu-alegand-un-primar-pas-primar-european-ne-apropiem-tot-mai-mult-de-aderarea-la-uniunea-europeana"
  //   },
  //   mainImage: {
  //     image: "https://unpaspentru.md/wp-content/webp-express/webp-images/uploads/2023/11/DSC00510-min-scaled.jpg.webp",
  //     blurDataURL: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg"
  //   },
  //   author: {
  //     name: "PAS",
  //     image: "https://unpaspentru.md/wp-content/uploads/2020/08/fav-1-100x100.png",
  //     slug: {
  //       current: "pas"
  //     }
  //   }
  // };
  // const post3 = {
  //   title: "Ilian Casu: socialistii din parlament si din consiliul municipal chisinau le au dublat locuitorilor capitalei impozitul pe imobile",
  //   publishedAt: new Date(Date.now()).toISOString(),
  //   slug: {
  //     current: "ilian-casu-socialistii-din-parlament-si-din-consiliul-municipal-chisinau-le-au-dublat-locuitorilor-capitalei-impozitul-pe-imobile"
  //   },
  //   mainImage: {
  //     image: "https://pnru.md/wp-content/uploads/2021/05/ilian_casu.jpg",
  //     blurDataURL: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg"
  //   },
  //   author: {
  //     name: "PNRU",
  //     image: "https://pnru.md/wp-content/themes/pnru/images/navbar/logo.jpg",
  //     slug: {
  //       current: "pnru"
  //     }
  //   }
  // };
  // //	
  // const post4 = {
  //   title: "Rebranding la democraţi: PDM devine Partidul Social Democrat European; Cine este liderul formațiunii",
  //   publishedAt: new Date(Date.now()).toISOString(),
  //   slug: {
  //     current: "live-congresului-al-x-lea-extraordinar-al-partidului-democrat-din-moldova"
  //   },
  //   mainImage: {
  //     image: "https://replicamedia.twic.pics/s3/2022-11-20/replica-38c77ce8256f0ab416a4308fd6396f8c_1280x720_fill.jpg",
  //     blurDataURL: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg"
  //   },
  //   author: {
  //     name: "PDM",
  //     image: "http://www.e-democracy.md/i/parties/pdm-logo.gif",
  //     slug: {
  //       current: "pdm"
  //     }
  //   }
  // };
  // const post5 = {
  //   title: "Președintele PSDE: Suntem a treia forță politică din R. Moldova",
  //   publishedAt: new Date(Date.now()).toISOString(),
  //   slug: {
  //     current: "presedintele-psde-suntem-a-treia-forta-politica-din-r-moldova"
  //   },
  //   mainImage: {
  //     image: "https://i.simpalsmedia.com/point.md/news/809x456/b0e1b4ac2359ecdcfa4ac05cd6a73b3f.jpg",
  //     blurDataURL: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg"
  //   },
  //   author: {
  //     name: "PSDE",
  //     image: "https://pes.eu/wp-content/uploads/2022/07/PSDE-Moldova-450x422.png",
  //     slug: {
  //       current: "psde"
  //     }
  //   }
  // };
  // //http://www.promis.md/_images/partide/pcrm.png
  // const post6 = {
  //   title: "Nicolae Pascaru: 'Voronin trebuie să fie inițiatorul unirii tuturor partidelor de stînga'",
  //   publishedAt: new Date(Date.now()).toISOString(),
  //   slug: {
  //     current: "nicolae-pascaru-voronin-trebuie-sa-fie-initiatorul-unirii-tuturor-partidelor-de-stinga"
  //   },
  //   mainImage: {
  //     image: "https://noi.md/uploads/newsthumbs/380_250/2023_08_08/696032.webp",
  //     blurDataURL: "https://www.tailwindtoolbox.com/products/tailus-alt.jpg"
  //   },
  //   author: {
  //     name: "PCRM",
  //     image: "http://www.promis.md/_images/partide/pcrm.png",
  //     slug: {
  //       current: "pcrm"
  //     }
  //   }
  // };
  // const posts = [
  //   post1, post2, post3, post4, post5, post6
  // ];
  return <HomePage posts={posts} />;
}

// export const revalidate = 60;
