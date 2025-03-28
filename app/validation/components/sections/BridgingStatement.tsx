"use client";

import { motion } from "framer-motion";

export default function BridgingStatement() {
  return (
    <section id="bridge" className="py-12 md:py-16">
      <motion.div 
        className="text-center"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
      >
        <h2 className="text-2xl md:text-3xl font-semibold">
          Get a transparent view of Investors.
        </h2>
      </motion.div>
    </section>
  );
} 