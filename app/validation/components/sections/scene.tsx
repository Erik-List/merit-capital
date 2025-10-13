"use client";

import { Suspense } from "react";
import {
  useGLTF,
  OrbitControls,
  Environment,
} from "@react-three/drei";
import { Canvas } from "@react-three/fiber";

export default function Scene() {
  return (
    <div className="w-full h-full relative">
      {/* Video background layer */}
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute inset-0 w-full h-full object-cover"
        style={{ zIndex: 0 }}
      >
        <source src="/backgrounds/validation/ocean bg video1.mp4" type="video/mp4" />
      </video>
      
      {/* 3D Canvas layer on top */}
      <Canvas 
        camera={{ position: [0, 1.8, 5], fov: 75 }}
        gl={{ alpha: true }}
        className="absolute inset-0"
        style={{ zIndex: 1 }}
      >
        <Suspense fallback={null}>
          <Environment preset="city" />
          <Model />
          <OrbitControls 
            target={[0, 0, 0]}
            enableZoom={false}
            enablePan={false}
            autoRotate={true}
            autoRotateSpeed={-2}
            enableDamping={true}
            dampingFactor={0.05}
          />
        </Suspense>
      </Canvas>
    </div>
  );
}

export function Model(props: any) {
  const { nodes, materials } = useGLTF('/models/merit-capital-3d.glb') as any
  return (
    <group {...props} dispose={null} scale={0.5}>
      <mesh geometry={nodes.Curve004.geometry} material={materials['Glass.003']} />
    </group>
  )
}

useGLTF.preload('/models/merit-capital-3d.glb')
